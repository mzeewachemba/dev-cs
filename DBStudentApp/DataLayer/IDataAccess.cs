using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DBStudentApp.DataLayer
{
    internal interface IDataAccess  //facade design pattern talking to DB
    {
        object GetSingleAnswer(string sql);
        DataTable GetManyRowsCols(string sql);
        int InsertUpdateDelete(String sql);
    }
}
