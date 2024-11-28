import pickle
import base64

data = input("Deserializer: ")
deserialized = pickle.loads(base64.b64decode(data))
print(deserialized)