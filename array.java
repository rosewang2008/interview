
//ArrayList with dynamic resizing
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

/*
hash table
bit array
O(n logn) time: string to character array, sort alphabetically, check if two consecutive elements equal
*/
public static boolean isUnique(String word) {
	if (word.length() > 26) {
		// by the Pidgeonhole principle--if word longer than 26
		// letter duplication is guaranteed 
		return false;
	}
	int wordChecker = 0;
	for (int i = 0; i < str.length(); i++) {

	}
}

System.out.println('a' - 'a')
