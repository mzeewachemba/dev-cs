namespace BridgePattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnBridgeBasic_Click(object sender, EventArgs e)
        {
            //calling on implementation A
            Abstraction abs = new Abstraction(new ImplementationA());
            string res1 = abs.Operation();
            string res2 = abs.OperationGreet("Bill");
            MessageBox.Show(res1 + "\n" + res2);

            //calling on implementation B
            abs = new Abstraction(new ImplementationB());
            res1 = abs.Operation();
            res2 = abs.OperationGreet("Bill");
            MessageBox.Show(res1 + "\n" + res2);
        }

        private void btnRefinedAbstraction_Click(object sender, EventArgs e)
        {
            //RefinedAbstraction extends abstraction
            RefinedAbstraction rabs = new RefinedAbstraction(new ImplementationA());
            string res1 = rabs.Operation();
            string res2 = rabs.OperationGreet("Bill");
            //Triggering the existing method in the implementation
            string res3 = rabs.OperationGreetTime("Sally");
            MessageBox.Show(res1 + "\n" + res2 + "\n" + res3);
        }
    }
}
