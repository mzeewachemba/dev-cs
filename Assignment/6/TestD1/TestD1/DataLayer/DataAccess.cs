using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace TestD1.DataLayer
{
    internal class DataAccess : IDataAccess
    {
        string connStr =
       ConfigurationManager.ConnectionStrings["MYDBCONN"].ConnectionString;
        public DataTable GetManyRowsCols(string sql)
        {
            SqlConnection conn = new SqlConnection(connStr);
            DataTable dt = new DataTable();
            try
            {
                conn.Open();
                SqlDataAdapter da = new SqlDataAdapter(sql, conn);
                da.Fill(dt);
            }
            catch { throw; }
            finally { conn.Close(); }
            return dt;
        }
        public object GetSingleAnswer(string sql)
        {
            SqlConnection conn = new SqlConnection(connStr);
            object obj = null;
            try
            {
                conn.Open();
                SqlCommand cmd = new SqlCommand(sql, conn);
                obj = cmd.ExecuteScalar();
            }
            catch { throw; }
            finally { conn.Close(); }
            return obj;
        }
        public int InsertUpdateDelete(string sql)
        {
            SqlConnection conn = new SqlConnection(connStr);
            int rows = 0;
            try
            {
                conn.Open();
                SqlCommand cmd = new SqlCommand(sql, conn);
                rows = cmd.ExecuteNonQuery();
            }
            catch { throw; }
            finally { conn.Close(); }
            return rows;
        }
    }
}