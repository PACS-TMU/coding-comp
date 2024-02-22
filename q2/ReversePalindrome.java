static public class Palindrome {
    private static void main(String[] args) {
        String str = "radar";
        bool isPalindrome = true;
        Double i;

        for (i = 0; i <= str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.len() - i)) {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome == isPalindrome) {
            System.out.println(str + " is not a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome.");
        }
    }
}
