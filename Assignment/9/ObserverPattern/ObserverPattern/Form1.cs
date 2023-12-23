namespace ObserverPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnObserver_Click(object sender, EventArgs e)
        {
            ConcreteSubjectGoog csgoog = new ConcreteSubjectGoog();
            ConcreteObserver co1 = new ConcreteObserver("Bill");
            csgoog.AddObserver(co1);
            ConcreteObserver co2 = new ConcreteObserver("Sally");
            csgoog.AddObserver(co2);
            csgoog.UpdatePrice(7.50);
        }
    }
}
