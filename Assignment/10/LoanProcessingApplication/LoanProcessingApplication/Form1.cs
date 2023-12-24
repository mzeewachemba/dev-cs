namespace AbstractFactoryPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnAbstractFactoryUS_Click(object sender, EventArgs e)
        {
            LoanFactory lf = new LoanFactoryUS();
            ICreditCheck icc = lf.CreateCreditCheck();
            IBalanceCheck ibc = lf.CreateBalanceCheck();
            BankInfo bi = new BankInfo();
            bi.BankName = "City Bank";
            bi.CheckingAccountNum = 1234;
            bi.SavingAccountNum = 12341;
            bi.FirstName = "Bill";
            bi.LastName = "Baker";
            List<BankInfo> BList = new List<BankInfo>();
            BList.Add(bi);
            double creditScore = icc.GetCreditScore("Bill", "baker");
            double balance = ibc.GetCurrentBalances(BList);
            MessageBox.Show("Credit Score for Bill = " + creditScore.ToString() + "\nBalance = " + balance.ToString());
        }

        private void btnAbstractFactoryCanada_Click(object sender, EventArgs e)
        {
            LoanFactory lf2 = new LoanFactoryCanada();
            ICreditCheck icc2 = lf2.CreateCreditCheck();
            IBalanceCheck ibc2 = lf2.CreateBalanceCheck();
            BankInfo bi2 = new BankInfo();
            bi2.BankName = "Bank of Canada";
            bi2.CheckingAccountNum = 66554;
            bi2.SavingAccountNum = 86865;
            bi2.FirstName = "Nancy";
            bi2.LastName = "Adams";
            List<BankInfo> BList2 = new List<BankInfo>();
            BList2.Add(bi2);
            double creditScore2 = icc2.GetCreditScore("Nancy", "Adams");
            double balance2 = ibc2.GetCurrentBalances(BList2);
            MessageBox.Show("Credit Score for Nancy (Canada) = " +
            creditScore2.ToString() + "\nBalance = " + balance2.ToString());
        }
    }
}
