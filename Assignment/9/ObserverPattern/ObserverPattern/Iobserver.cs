using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ObserverPattern
{
    interface IObserver //subscriber/client
    {
        void Notify(StockInfo sinfo);
    }
}
