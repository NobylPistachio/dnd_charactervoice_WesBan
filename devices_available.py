from soundOutput import put_test
from pyaudio import PyAudio

# def get_device_info():
#     player = PyAudio()
#     devicelist = []
#     for hostApiIndex in range(10):
#         for hostApiDeviceIndex in range(10): 
#             try:
#                 a = player.get_device_info_by_host_api_device_index(hostApiIndex,hostApiDeviceIndex)["name"]
#                 if a not in devicelist:
#                     devicelist.append(a)
#             except:
#                 print(f"{hostApiIndex},{hostApiDeviceIndex} - No Device")
#     print(devicelist)

def output_device_stats():
    
    print(f"{list(PyAudio().get_device_info_by_index(0).keys())}")
    


def get_audio_device_info():
    devicelist = []
    user = PyAudio()
    index = 0
    while True:
        try: 
            device = user.get_device_info_by_index(index)['name']
            devicelist.append(device)
            index += 1
        except:
            break
    print(devicelist)

get_audio_device_info()
# output_device_stats()

# if __name__ == "__main__":
#     put_test("In")
#     put_test("Out")