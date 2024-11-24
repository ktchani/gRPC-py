from concurrent import futures
import grpc
from proto import service_pb2, service_pb2_grpc

class UserResponseService(service_pb2_grpc.MyServiceServicer):

    def GetUserResponse(self, request, context):
        """Unary RPC
        """
        response = service_pb2.UserResponse(
            message=f'Hello {request.name}',
            success=True,
            age=25,
            height=166
        )
        return response

    def StreamData(self, request, context):
        """Server streaming
        """
        response = service_pb2.UserResponse(
            message=f'Hello sirrr {request.name}',
            success=True,
            age=25,
            height=172
        )
        for _ in range(10):
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(UserResponseService(), server)
    server.add_insecure_port('[::]:50051')
    print('Starting server. Listening on port 50051.')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()