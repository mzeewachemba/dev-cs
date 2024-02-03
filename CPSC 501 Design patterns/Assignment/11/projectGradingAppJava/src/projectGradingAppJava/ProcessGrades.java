package projectGradingAppJava;

//imports
import java.util.ArrayList; 
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.FileReader;

public class ProcessGrades implements IProcessGrades {

	//list of students
	ArrayList<Student> STList = new ArrayList<Student>();

	public void readStudentData(String inputFileName) throws Exception
	{ // will read students into the STList
		FileReader file = new FileReader(inputFileName);
		BufferedReader sr = new BufferedReader(file);
		try
		{
			STList.clear(); // clear the list of students

			String sline = sr.readLine();
			while (sline != null)
			{
				Student st = null; // base class reference
				String[] parts = sline.split("\t");
				if (parts.length == 6) // undergrad student
				{
					if (parts[3].toUpperCase().equals("UNDERGRAD"))
					{
						st = (Student) new UnderGradStudent(Integer.parseInt(parts[0]),
								parts[1],
								parts[2], Integer.parseInt(parts[4]),
								Integer.parseInt(parts[5]));
					}
				}
				if (parts.length == 7) // grad student
				{
					if (parts[3].toUpperCase().equals("GRADUATE"))
					{
						st = (Student) new GradStudent(Integer.parseInt(parts[0]),
								parts[1],
								parts[2], Integer.parseInt(parts[4]),
								Integer.parseInt(parts[5]), parts[6]);
					}
				}
				if (parts.length == 9) // Phd student
				{
					if (parts[3].toUpperCase().equals("PHDCPSC"))
					{
						st = (Student) new PhdStudent(Integer.parseInt(parts[0]),
								parts[1],
								parts[2], Integer.parseInt(parts[5]),
								Integer.parseInt(parts[6]), parts[7], parts[8]);
					}
				}
				if (st != null)
					STList.add(st); // add student to the list
				sline = sr.readLine(); // read next line
			}
		}
		catch (Exception ex)
		{
			throw ex; // if error, send error back to the calling code
		}
		finally
		{
			sr.close();
		}
	}
	
	public void processAndWriteGrades(String outFileName) throws Exception
	{
		FileWriter file = new FileWriter(outFileName);
		BufferedWriter sw = new BufferedWriter(file);
		try
		{
			STList.sort(null);
			for(Student st:STList) {
				String grade = st.computeGrade();
				// polymorphism, correct ComputeGrade
				// will be called depending upon the type of student in st
				sw.write(st.id + "\t" + grade);
				sw.newLine();
			}
			sw.close();
		}
		catch(Exception ex)
		{
			throw ex;
		}
		finally
		{
			sw.close();
		}
	}
}
