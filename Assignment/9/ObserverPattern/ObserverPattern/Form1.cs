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
            ConcreteSubjectGoog csgoog = new ConcreteSubjectGoog(); //creating a publisher
            ConcreteObserver co1 = new ConcreteObserver("Bill"); //creating observer
            csgoog.AddObserver(co1); // adding observer
            ConcreteObserver co2 = new ConcreteObserver("Sally");
            csgoog.AddObserver(co2);
            csgoog.UpdatePrice(7.50);//updating prices and notification will be sent automatically
        }
    }
}
