namespace DecoratorPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnDecoratorSimple_Click(object sender, EventArgs e)
        {
            //allow to choose and excecute different enhancements enhancement
            IComponent cmp = new Component();
            // base system object - undecorated - Component only
            MessageBox.Show("Orig component:\n" + cmp.Welcome("Bill"));
            // after decoration by DecoratorTime
            DecoratorTime dect = new DecoratorTime(cmp);
            // decorates cmp with time info - uses base component cmp
            MessageBox.Show("Time decoration:\n" + dect.Welcome("Bill"));
            // after decoration by DecoratorBday only - uses base component cmp
            DecoratorBday decb = new DecoratorBday(cmp);
            MessageBox.Show("Bday decoration:\n" + decb.Welcome("Bill"));
            //COMBINING DATA AND TIME
            // decoration by both time and bday
            DecoratorBday decTimeBday = new DecoratorBday(dect);
            MessageBox.Show("Time,Bday decoration:\n" + decTimeBday.Welcome("Bill"));
        }

        private void btnSubClassing_Click(object sender, EventArgs e)
        {
            ComponentDerivedTime cdt = new ComponentDerivedTime();
            MessageBox.Show(cdt.Welcome());
            ComponentDerivedBday cdb = new ComponentDerivedBday();
            MessageBox.Show(cdb.Welcome());

            MessageBox.Show(cdt.Welcome() + cdb.Welcome()); 
            //this will produce duplicates information in the output which is not a desired output
            //using normal inheritence will require more classes so that we can combine/choose desired features
        }
    }
}
