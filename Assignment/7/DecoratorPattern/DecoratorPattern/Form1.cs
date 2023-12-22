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
            IComponent cmp = new Component();
            // base system object - undecorated
            MessageBox.Show("Orig component:\n" + cmp.Welcome("Bill"));
            // after decoration by DecoratorTime
            DecoratorTime dect = new DecoratorTime(cmp);
            // decorates cmp with time info
            MessageBox.Show("Time decoration:\n" + dect.Welcome("Bill"));
            // base component after decoration by DecoratorBday only
            DecoratorBday decb = new DecoratorBday(cmp);
            MessageBox.Show("Bday decoration:\n" + decb.Welcome("Bill"));
            // after decoration by both time and bday
            DecoratorBday decTimeBday = new DecoratorBday(dect);
            MessageBox.Show("Time,Bday decoration:\n" + decTimeBday.Welcome("Bill"));
        }

        private void btnSubClassing_Click(object sender, EventArgs e)
        {
            ComponentDerivedTime cdt = new ComponentDerivedTime();
            MessageBox.Show(cdt.Welcome());
            ComponentDerivedBday cdb = new ComponentDerivedBday();
            MessageBox.Show(cdb.Welcome());
            // what if we wanted both time and bday decoration
            // This will require us to create another derived class
            // what if we wanted to print out time first, then bday
            // or vice versa. This will require us to create many
            // subclasses. Following does not produce desired
        }
    }
}
