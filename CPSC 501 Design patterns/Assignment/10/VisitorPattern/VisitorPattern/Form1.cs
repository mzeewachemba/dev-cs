namespace VisitorPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnVisitor_Click(object sender, EventArgs e)
        {
            Employees emps = new Employees();
            AdminAssistant aa = new AdminAssistant("Bill", 10, 35000);
            emps.Add(aa);
            Manager mn = new Manager("Sally", 15, 75000);
            emps.Add(mn);
            VicePresident vp = new VicePresident("Mark", 20, 95000);
            emps.Add(vp);
            BonusVisitor ivis = new BonusVisitor();
            emps.Accept(ivis);

            VacationVisitor vv = new VacationVisitor();
            emps.Accept(vv);
            string out1 = "";
            foreach (Employee ee in emps.EList)
                out1 += ee.ToString() + "\n";
            MessageBox.Show(out1);

        }

        private void btnAddComputePayMethod_Click(object sender, EventArgs e)
        {
            Employee2 em = new Employee2("John Jacobs", 52, 15);
            ComputePayVisitor cpv = new ComputePayVisitor();
            double res = em.Accept(cpv);
            MessageBox.Show(res.ToString());
        }

        private void btnAddOverTime_Click(object sender, EventArgs e)
        {
            Employee2 em = new Employee2("John Jacobs", 52, 15);
            OverTimeVisitor otv = new OverTimeVisitor();
            double res = em.Accept(otv);
            MessageBox.Show("OverTime Pay = " + res.ToString());
        }

        private void btnOverTimeExtension_Click(object sender, EventArgs e)
        {
            Employee2 e2 = new Employee2("John Jacobs", 52, 15);
            double res = e2.ComputeOverTime();
            MessageBox.Show("OverTime Pay = " + res.ToString());
        }
    }
}
