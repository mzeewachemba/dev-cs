package projectGradingAppJava;

//child class to student class
public class PhdStudent extends Student{
	// id, firstName, lastName, test1, test2 are inherited from Student
	String dissertation; // added extra field in PhdStudent class
	String advisor; // added extra field in PhdStudent class

	public PhdStudent(int id, String fname, String lname, int test1, int test2, String dissertation, String advisor)
	{// delegating properties initialization to base class constructor for first 5 fields
		super(id, fname, lname, test1, test2);
		this.dissertation = dissertation; // initialization of extra field
		this.advisor = advisor; // initialization of extra field
	}

	@Override 
	public String computeGrade()
	{
		double avg = 0.4 * test1 + 0.6 * test2;
		String grade = "";
		if (avg > 95) // more than 95 is an A for a PhdStudent
			grade = "A";
		else if (avg > 90)
			grade = "A-";
		else if (avg > 87)
			grade = "B+";
		else if (avg > 80)
			grade = "B";
		else
			grade = "C";
		return grade;
	}
}

