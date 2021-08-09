using Microsoft.Azure.Devices;
using Microsoft.Azure.Devices.Common.Exceptions;
using System;
using System.Diagnostics;
using System.Threading.Tasks;

namespace IotHub.CreateDeviceId
{
    class CreateDeviceIdApp
    {
        private readonly RegistryManager registryManager;
        private readonly string connectionString;
        private readonly string deviceId;

        public CreateDeviceIdApp(string deviceId, string connectionString)
        {
            this.deviceId = "TestDevice1";
            this.connectionString = connectionString;
            this.registryManager = RegistryManager.CreateFromConnectionString(this.connectionString);
        }

        static void Main(string[] args)
        {
            TraceListener consoleTraceListener = new ConsoleTraceListener();
            Trace.Listeners.Add(consoleTraceListener);

            CreateDeviceIdApp app = new CreateDeviceIdApp("TestDevice1", "HostName=pknu-iot-dps.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=UoTvHIhJ7ixdd62aWUk/Uw1fVo9KsDBi+iYSor0I5dc=");
            app.AddDeviceAsync().Wait();
            Console.ReadKey();
        }

        private async Task AddDeviceAsync()
        {
            Device device = null;
            try
            {
                device = await this.registryManager.AddDeviceAsync(new Device(this.deviceId));
                Trace.WriteLine(string.Format("Generated device key: {0}", device.Authentication.SymmetricKey.PrimaryKey));
            } 
            catch (DeviceAlreadyExistsException)
            {
                device = await this.registryManager.GetDeviceAsync(this.deviceId);
                Trace.WriteLine(String.Format("Fetch existing deivce key: {0}", device.Authentication.SymmetricKey.PrimaryKey));
            }
            catch (Exception ex)
            {
                Trace.WriteLine(String.Format("Unexpected exception {0}", ex));
            }
        }
    }
}
