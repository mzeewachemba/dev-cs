package projectGradingAppJava;

public interface IProcessGrades {
	void readStudentData(String inputFileName) throws Exception;
	void processAndWriteGrades(String outFileName) throws Exception;
}
