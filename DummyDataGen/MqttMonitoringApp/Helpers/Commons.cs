using System.Globalization;
using System.Windows.Controls;
using uPLibrary.Networking.M2Mqtt;

namespace MqttMonitoringApp.Helpers
{
    public class Commons
    {
        public static string BROKERHOST { get; set; }
        public static string PUB_TOPIC { get; set; }  // home/device/data
        public static MqttClient BROKERCLIENT { get; set; }
        public static string CONNSTRING { get; set; }
        public static bool ISCONNECT { get; set; }
    }

    public class NotEmptyValidationRule : ValidationRule
    {
        public override ValidationResult Validate(object value, CultureInfo cultureInfo)
        {
            return string.IsNullOrWhiteSpace((value ?? "").ToString())
                ? new ValidationResult(false, "Field is required.")
                : ValidationResult.ValidResult;
        }
    }
}
