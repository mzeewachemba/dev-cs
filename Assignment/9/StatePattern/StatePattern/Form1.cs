namespace StatePattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTestStatePattern_Click(object sender, EventArgs e)
        {
            // client interacts with the context i.e., CheckingAccount
            CheckingAccount acct = new CheckingAccount("Bill", 1234);
            //acct.DepositMoney(1200);
            //acct.WithDrawMoney(500);
            acct.DepositMoney(6000);
            MessageBox.Show(acct.State.ToString());
        }
    }
}
