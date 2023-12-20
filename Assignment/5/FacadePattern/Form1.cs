using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FacadePattern
{
    public partial class fmMortgage1 : Form
    {
        public fmMortgage1()
        {
            InitializeComponent();
        }

        private void btnMortgageApproval_Click(object sender, EventArgs e)
        {
            string reason = "";
            MortgageApplicant mapp = new MortgageApplicant
            {
                FirstName = "Bill",
                LastName = "Baker",
                BankAccountNum = 12345,
                LoanAccountNum = 12345,
                SSNum = "111-22-3333",
                LoanAmountAsked = 150000
            };

            //enhacing form class
            //using non singleton object
            //MortgageFacade mf = new MortgageFacade();

            //using singleton object, without new keyword
            MortgageFacadeSingleton mf = MortgageFacadeSingleton.Instance;
            bool approved = mf.MortgageApproval(mapp,ref reason);
            if (approved == true)
                MessageBox.Show("Your application has been approved..");
            else
                MessageBox.Show("Your application has been denied..\n" +
                reason);

        }
    }
}
