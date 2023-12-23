using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;


namespace ProxyPattern
{
    //need authentication to access this class
    internal class DataAccessFacade
    {
        public string CONNSTR = "server=DESKTOP-Q1L8NT0\\SQLEXPRESS;integrated security=true;database=ProductsBCBS";
        
        public object GetSingleAnswer(string sql)
        {
            SqlConnection conn = new SqlConnection(CONNSTR);
            object obj = null;
            try
            {
                conn.Open();
                SqlCommand cmd = new SqlCommand(sql, conn);
                obj = cmd.ExecuteScalar();
            }
            catch (Exception)
            {
                throw;
            }
            finally
            {
                conn.Close();
            }
            return obj;
        }
        public int UpdateInsertDelete(string sql)
        {
            SqlConnection conn = new SqlConnection(CONNSTR);
            int rowsModified = 0;
            try
            {
                conn.Open();
                SqlCommand cmd = new SqlCommand(sql, conn);
                rowsModified = cmd.ExecuteNonQuery();
            }
            catch (Exception)
            {
                throw;
            }
            finally
            {
                conn.Close();
            }
            return rowsModified;
        }

        public DataTable GetManyRowsCols(string sql)
        {
            SqlConnection conn = new SqlConnection(CONNSTR);
            DataTable dt = new DataTable();
            try
            {
                conn.Open();
                SqlDataAdapter da = new SqlDataAdapter(sql, conn);
                da.Fill(dt);
                conn.Close();
            }
            catch (Exception)
            {
                throw;
            }
            finally
            {
                conn.Close();
            }
            return dt;
        }
    }
}
