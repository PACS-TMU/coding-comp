// Create a program that checks if a given string is a palindrome.
// A palindrome is a word, phrase, number, or other sequence of characters that reads the
// same forward and backward (given that there are no spaces or punctuations).
// NOTE: Case should be ignored when checking if a string is a palindrome.
public class AnswerPalindrome {
    public boolean isPalindrome(String input) {
        String str = input.toLowerCase();
        String reversedStr = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            reversedStr += str.charAt(i);
        }
        return str.equals(reversedStr);
    }
    public static void main(String[] args) {
        // Test the isPalindrome method
        TestCasesPalindrome test = new TestCasesPalindrome();
        test.testAll();
    }
}