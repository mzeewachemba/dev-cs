package projectGradingAppJava;

public abstract class Student implements Comparable<Student>{

	//student variables
	int id;
	String firstName;
	String lastName;
	int test1;
	int test2;

	//public constructor
	public Student(int id, String fname, String lname, int test1, int test2)
	{ 
		this.id = id;
		this.firstName = fname;
		this.lastName = lname;
		this.test1 = test1;
		this.test2 = test2;
	}

	@Override
	public int compareTo(Student st) {
		// below code is negated to reverse natural order
		return - 1*Double.valueOf(getGradePoints(this.computeGrade())).compareTo(Double.valueOf(getGradePoints(st.computeGrade())));
	}

	//this method generates point depending on the grades
	double getGradePoints(String grade){
		double points = 0;
		switch (grade)
		{
		case "A": 
			points = 4.0;
			break;
		case "A-":
			points = 3.7;
			break;
		case "B+":
			points = 3.3;
			break;
		case "B":
			points = 3.0;
			break;
		case "B-":
			points = 2.7;
			break;
		case "C+":
			points = 2.3;
			break;
		case "C":
			points = 2.0;
			break;
		default:
			points = 1.0;
			break;
		}
		return points;
	}

	public abstract String computeGrade(); // child class to provide an implemetation

}
