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
            MessageBox.Show(e2.Addr.StreetAddress);//e2 will have an address of e1

            MessageBox.Show(e1.Addr.StreetAddress);//e1 will have the new address "25 Taco Lane"

        }

        private void btnTestPrototypeManager_Click(object sender, EventArgs e) //enhanced prototype, allows to retrive values using dictionary
        {
            EmployeeCopyManager emg = new EmployeeCopyManager();
            Employee e1 = emg["Austin"];//creating a copy
            MessageBox.Show(e1.Addr.StreetAddress);
        }
    }
}