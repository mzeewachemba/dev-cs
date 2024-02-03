package projectGradingAppJava;

//undergrad class derives student class
public class UnderGradStudent extends Student { //uses extends
	public UnderGradStudent(int id, String fname, String lname, int test1,int test2) { 
		// delegate properties initialization to base class constructor
		super(id,fname,lname,test1,test2);
	}
	// id, fFirstName, lastName, test1, test2 are inherited from Student
	@Override //annotation for overriding
	public String computeGrade() // Override is with captial O
	{
		double avg = 0.4 * test1 + 0.6 * test2;
		String grade = "";
		if (avg > 90)
			grade = "A";
		else if (avg > 85)
			grade = "A-";
		else if (avg > 80)
			grade = "B+";
		else if (avg > 70)
			grade = "B";
		else
			grade = "C";
		return grade;
	}

}
