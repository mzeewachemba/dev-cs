package projectGradingAppJava;

//child of student class
public class GradStudent extends Student {
	String thesis; // added extra field in GradStudent class

	public GradStudent(int id, String fname, String lname, int test1, int test2, String thesis){
		// delegating properties initialization to base class constructor for first 5 fields
		super(id, fname, lname, test1, test2);
		this.thesis = thesis; // initialization of extra field
	}

	// id, firstName, lastName, test1, test2 are inherited from Student
	
	@Override 
	public String computeGrade()
	{
		double avg = 0.4 * test1 + 0.6 * test2;
		String grade = "";
		if (avg > 92) // more than 92 is an A for a GradStudent
			grade = "A";
		else if (avg > 87)
			grade = "A-";
		else if (avg > 83)
			grade = "B+";
		else if (avg > 75)
			grade = "B";
		else
			grade = "C";
		return grade;
	}
}
