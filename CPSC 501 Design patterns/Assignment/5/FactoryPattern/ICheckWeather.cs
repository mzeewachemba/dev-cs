using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryPattern
{
    internal interface ICheckWeather
    {
        double GetCurrentTemperature(string zipcode);
        string CheckNextDayForecast(string city, string state);
    }
}
