namespace PrototypePattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnProtoType_Click(object sender, EventArgs e)
        {
            Address a1 = new Address
            {
                StreetAddress = "55 Pizza Lane",
                City = "Austin"
            };
            Employee e1 = new Employee();
            e1.FirstName = "Bill";
            e1.LastName = "Baker";
            e1.EmployeeId = 12345;
            e1.Addr = a1;
            Employee e2 = e1.Copy();
            e1.Addr.StreetAddress = "25 Taco Lane";
            MessageBox.Show(e2.Addr.StreetAddress);
        }

        private void btnTestPrototypeManager_Click(object sender, EventArgs e)
        {
            EmployeeCopyManager emg = new EmployeeCopyManager();
            Employee e1 = emg["Austin"];
            MessageBox.Show(e1.Addr.StreetAddress);
        }
    }
}