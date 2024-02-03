using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestD1.DataLayer
{
    internal class DataAccessMySql : IDataAccess
    {
        //mysql implementation
        string connStr = ConfigurationManager.ConnectionStrings["MYDBCONNMYSQL"].ConnectionString;
        public DataTable GetManyRowsCols(string sql)
        {
            MySqlConnection conn = new MySqlConnection(connStr);
            DataTable dt = new DataTable();
            try
            {
                conn.Open();
                MySqlDataAdapter da = new MySqlDataAdapter(sql, conn);
                da.Fill(dt);
            }
            catch { throw; }
            finally { conn.Close(); }
            return dt;
        }
        public object GetSingleAnswer(string sql)
        {
            MySqlConnection conn = new MySqlConnection(connStr);
            object obj = null;
            try
            {
                conn.Open();
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                obj = cmd.ExecuteScalar();
            }
            catch { throw; }
            finally { conn.Close(); }
            return obj;
        }
        public int InsertUpdateDelete(string sql)
        {
            MySqlConnection conn = new MySqlConnection(connStr);
            int rows = 0;
            try
            {
                conn.Open();
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                rows = cmd.ExecuteNonQuery();
            }
            catch { throw; }
            finally { conn.Close(); }
            return rows;
        }
    }
}
