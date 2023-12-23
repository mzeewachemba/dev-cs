using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProxyPattern
{
    internal class ProtectionProxy
    {
        DataAccessFacade daf = null;
        public bool Authenticate(string password)
        {
            bool res = false;
            if (password == "secret")
            {
                daf = new DataAccessFacade();
                res = true;
            }
            return res;
        }

        //below methods will only work if anthentication passes
        public object GetSingleAnswer(string sql)
        {
            object obj = null;
            if (daf != null)
                obj = daf.GetSingleAnswer(sql);
            else
                throw new Exception("requires authentication..");
            return obj;
        }
        public int UpdateInsertDelete(string sql)
        {
            int ret = 0;
            if (daf != null)
                ret = daf.UpdateInsertDelete(sql);
            else
                throw new Exception("requires authentication..");
            return ret;
        }

        public DataTable GetManyRowsCols(string sql)
        {
            DataTable dt = null;
            if (daf != null)
                dt = daf.GetManyRowsCols(sql);
            else
                throw new Exception("requires authentication..");
            return dt;
        }
    }
}
