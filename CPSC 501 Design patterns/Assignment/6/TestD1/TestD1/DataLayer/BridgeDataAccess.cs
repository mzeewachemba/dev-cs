using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestD1.DataLayer
{
    internal class BridgeDataAccess : IDataAccess
    {
        IDataAccess _idac = null;
        //aggregation
        public BridgeDataAccess(IDataAccess idac) { _idac = idac; }
        public DataTable GetManyRowsCols(string sql)
        {
            return _idac.GetManyRowsCols(sql);
        }
        public object GetSingleAnswer(string sql)
        {
            return _idac.GetSingleAnswer(sql);
        }
        public int InsertUpdateDelete(string sql)
        {
            return (_idac.InsertUpdateDelete(sql));
        }
    }
}
