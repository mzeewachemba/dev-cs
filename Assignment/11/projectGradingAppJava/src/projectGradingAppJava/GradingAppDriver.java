package projectGradingAppJava;

public class GradingAppDriver {
	public static void main(String[] args) {
		try
		{
			String inputFile = "F:/CPSC501/data_3/StudentsData.txt";
			String outputFile = "F:/CPSC501/data_3/StudentGrades.txt";
			ProcessGrades pg = new ProcessGrades();
			pg.readStudentData(inputFile);
			pg.processAndWriteGrades(outputFile);
			System.out.println("Grades processed, examine file " +
					outputFile);
		}
		catch (Exception ex)
		{
			System.out.println(ex.getMessage());
		}
	}
}