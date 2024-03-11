public class AnswerCountAndSay {
    /*
     * Count and Say Sequence
     * Implement a program where you count the number of consecutive digits in a string.
     * For example: "111112230", the function should return "51221310"
     * To run the program, run javac Answer.java TestCases.java in terminal
     * Then java Answer.java in terminal
     * Make sure to create an algorithm that runs in O(n) to get full points for this question.
     * In other words, make sure there are no nested loops.
     */
    public String sayCount(String digits) {
        if (digits == null || digits.isEmpty()) {
            return "";
        }

        String say = "";
        int count = 1;

        for (int i = 1; i < digits.length(); i++) {               
            if (digits.charAt(i) == digits.charAt(i - 1)) {
                count++;
            } else {
                say += count + "" + digits.charAt(i - 1);
                count = 1;
            }
        }
        say += count + "" + digits.charAt(digits.length() - 1);
        
        return say;   
    }

    public static void main(String[] args) {
        TestCasesCountAndSay test = new TestCasesCountAndSay();
        test.testAll();
    }
}
