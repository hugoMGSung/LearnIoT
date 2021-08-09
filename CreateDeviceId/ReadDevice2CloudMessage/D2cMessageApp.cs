using Microsoft.ServiceBus.Messaging;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace IotHub.ReadDevice2CloudMessage
{
    class D2cMessageApp
    {
        private readonly string connectionString;
        private readonly string iotHubD2cEndpoint;
        private readonly EventHubClient eventHubClient;

        public D2cMessageApp(string connectionString, string iotHubD2cEndpoint)
        {
            this.connectionString = connectionString;
            this.iotHubD2cEndpoint = iotHubD2cEndpoint;
            this.eventHubClient = EventHubClient.CreateFromConnectionString(
                this.connectionString, this.iotHubD2cEndpoint);
        }

        static void Main(string[] args)
        {
            TraceListener consoleTraceListener = new ConsoleTraceListener();
            Trace.Listeners.Add(consoleTraceListener);

            D2cMessageApp app = new D2cMessageApp(
                "HostName=pknu-iot-dps.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=UoTvHIhJ7ixdd62aWUk/Uw1fVo9KsDBi+iYSor0I5dc=", "messages/events");

            string[] d2cPartitions = app.eventHubClient.GetRuntimeInformation().PartitionIds;
            CancellationTokenSource cts = new CancellationTokenSource();

            List<Task> tasks = new List<Task>();
            foreach (string partition in d2cPartitions)
            {
                tasks.Add(app.ReceiveDevice2CloudMessageAsync(partition, cts.Token));
            }
            Task.WaitAll(tasks.ToArray());
        }

        private async Task ReceiveDevice2CloudMessageAsync(string partition, CancellationToken token)
        {
            EventHubReceiver eventHubReceiver = this.eventHubClient
                .GetDefaultConsumerGroup().CreateReceiver(partition, DateTime.UtcNow);
            while (true)
            {
                if (token.IsCancellationRequested) break;
                EventData eventData = await eventHubReceiver.ReceiveAsync();
                if (eventData == null) continue;

                string data = Encoding.UTF8.GetString(eventData.GetBytes());
                Trace.WriteLine(string.Format("Message received. Partition: {0} Data : {1}", partition, data));
            }
        }
    }
}
