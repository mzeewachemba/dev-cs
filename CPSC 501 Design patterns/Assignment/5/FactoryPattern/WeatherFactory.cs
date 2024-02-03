using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryPattern
{
    //this class will decide which object to return depending on the type of Forecast accuracy
    internal class WeatherFactory
    {
        public static ICheckWeather CreateWeatherInfo(ForecastAccuracy wtype)
        {
            ICheckWeather icw = null;
            if (wtype == ForecastAccuracy.FAIR)
            {
                icw = new WeatherNOAA();
            }
            if (wtype == ForecastAccuracy.GOOD)
            {
                icw = new WeatherYahoo();
            }
            return icw;
        }
    }
}
