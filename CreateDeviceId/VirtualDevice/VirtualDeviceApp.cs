using Microsoft.Azure.Devices.Client;
using Newtonsoft.Json;
using System;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;

namespace IoTHub.VirtualDevice
{
    class VirtualDeviceApp
    {
        private static Random Rand = new Random();
        private readonly DeviceClient deviceClient;
        private string deviceId;
        private string iotHubUri;
        private string deviceKey;

        public VirtualDeviceApp(string deviceId, string iotHubUri, string deviceKey)
        {
            this.deviceId = deviceId;
            this.iotHubUri = iotHubUri;
            this.deviceKey = deviceKey;
            this.deviceClient = DeviceClient.Create(
                this.iotHubUri,
                new DeviceAuthenticationWithRegistrySymmetricKey(this.deviceId, this.deviceKey), TransportType.Mqtt);
        }

        static void Main(string[] args)
        {
            TraceListener consoleTraceListener = new ConsoleTraceListener();
            Trace.Listeners.Add(consoleTraceListener);

            // 디바이스 상세에서 확인
            VirtualDeviceApp deviceApp = new VirtualDeviceApp("TestDevice1", "pknu-iot-dps.azure-devices.net",
                "bUR6l82/4H/DGmF45pmIQzD9reK6kvgB927PzmK8tgo=");
            Console.WriteLine("Virtual deivce is created.\n");
            deviceApp.SendDevice2CloudMessagesAsync();
            Console.ReadKey();
        }

        private async void SendDevice2CloudMessagesAsync()
        {
            double temperatureInCelSius = 30;

            while (true)
            {
                double temperature = temperatureInCelSius + Rand.NextDouble() * 5;
                var dataSample = new
                {
                    deviceId = this.deviceId,
                    temperature = temperature,
                    guid = Guid.NewGuid().ToString()
                };

                string messageString = JsonConvert.SerializeObject(dataSample);
                Message message = new Message(Encoding.ASCII.GetBytes(messageString));

                await this.deviceClient.SendEventAsync(message);
                Trace.WriteLine(string.Format("{0}, Sending message: {1}", DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"), messageString));

                await Task.Delay(1000);               
            }
        }
    }
}
