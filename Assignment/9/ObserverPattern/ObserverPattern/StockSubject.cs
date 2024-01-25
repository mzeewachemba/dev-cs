using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ObserverPattern
{
    internal class StockSubject //publisher
    {
        List<IObserver> OBList = new List<IObserver>(); //maintains list of subscribers
        StockInfo stockInfo = null;
        public StockSubject(StockInfo sinfo) //stock itself
        {
            stockInfo = sinfo;
        }
        //has access to update the prices
        public void UpdatePrice(double updateAmt)
        {
            stockInfo.Price = stockInfo.Price + updateAmt;
            // notify observers i.e., subscribers
            foreach (IObserver observer in OBList)
                observer.Notify(stockInfo); // send state of stock to subscribers
        }
        public void AddObserver(IObserver obs)
        {
            OBList.Add(obs);
        }
        public void RemoveObserver(IObserver obs)
        {
            OBList.Remove(obs);
        }
    }
}
