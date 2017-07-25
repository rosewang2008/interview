
public class array {
/*
ArrayList with dynamic resizing
*/
//amortized insertion runtime

	ArrayList<String> sentence = new ArrayList<String>();
	for (String w : words) sentence.add(w);
	for (String w : more) sentence.add(w);
	return sentence;
	
	String joinWords(String[] words){
		String sentence = "";
		for (String w : words) {
			sentence = sentence + w; 
		}
		return sentence;
	}

	String StringBuilderFunction(String[] words) {
		StringBuilder sentence = new StringBuilder();
		for (String w : words) { 
			sentence.append(w);
		}
		return sentence.toString();
		// why would you need to turn entire sentence to string again?
	}
/*
StringBuilder: avoids long runtime for string concatenation
*/
	

	public static void main (String[] args) {
		System.out.println(StringBuilderFunction(['fine', 'ok']))
	}
}
/*
StringBuilder: avoids long runtime for string concatenation
*/
