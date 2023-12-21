using Org.BouncyCastle.Crypto;
using System.Data;
using TestD1.DataLayer;

namespace TestD1
{
    public partial class Form1 : Form
    {
        //SWITCHING IMPLEMENTATION
        //IDataAccess idac = new BridgeDataAccess(new DataAccessMySql());
        IDataAccess idac = new BridgeDataAccess(new DataAccess());
        public Form1()
        {
            InitializeComponent();
        }

        private void cmbCategories_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                var cat = cmbCategories.SelectedValue;
                if (cat.GetType().Name != "Int32")
                    return;
                string catid = cmbCategories.SelectedValue.ToString();
                string sql = "select * from Products where CategoryId=" + catid;
                DataTable dt = idac.GetManyRowsCols(sql);
                dg1.DataSource = dt;
                dg1.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                string sql = "select * from categories";
                DataTable dt = idac.GetManyRowsCols(sql);
                cmbCategories.DataSource = dt;
                cmbCategories.ValueMember = "CategoryID";
                cmbCategories.DisplayMember = "CategoryName";
                cmbCategories.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
