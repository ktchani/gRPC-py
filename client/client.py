import grpc
from proto import service_pb2_grpc, service_pb2

def run():
    with grpc.insecure_channel('host.docker.internal:50051') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)

        # Non streaming call
        request = service_pb2.RequestUser(name='John Doe')
        response = stub.GetUserResponse(request)
        print("Sync response received: " + response.message)

        # Streaming call
        request = service_pb2.RequestUser(name='John Doe')
        responses = stub.StreamData(request)
        for response in responses:
            print("Async response received: " + response.message)


if __name__ == "__main__":
    run()