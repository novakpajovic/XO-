import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.math.BigDecimal;
import java.util.*;

public class TicTacToeValidCombinations {
    private static char SPACE = ' ';

    HashSet<String> myBoards = new HashSet<String>();

    public void addCombinations()
    {
    	try(PrintWriter out = new PrintWriter("tic-tac-toe-4.csv"))
    	{
    		int validCombinations = 0;
		    for (long i = 0; i < 4294967296L && validCombinations < 5000; i++)
			{
		    	long c = i;
		    	StringBuilder strBuilder = new StringBuilder();
				for (int j = 0; j < 16; ++j)
				{
					if(c % 4 == 0)
						strBuilder.append("B");
					else if(c % 4 == 1)
						strBuilder.append("X");
					else if(c%4 == 2)
						strBuilder.append("O");
					else if(c%4 == 3)
						strBuilder.append("+");
					
					c /= 4;
				}
				
				String combination = strBuilder.toString();
				char[] combArray = combination.toCharArray();
				if(isValid(combArray))
				{
					StringBuilder strBuilder1 = new StringBuilder();
					
					for(int count=0; count<combArray.length; count++)
					{
						strBuilder1.append(combArray[count]);
						strBuilder1.append(',');
					}
					
					if(isCWin(combArray,'+'))
					{
						strBuilder1.append("TRUE");
						
					}
					else
					{
						strBuilder1.append("FALSE");
						validCombinations++;
						myBoards.add(strBuilder1.toString());
						
					;
						
					}
					
					
					
					
					
				}
			}
		} catch (FileNotFoundException e) {
			
			e.printStackTrace();
		}
    }
    
    public void outputToFile()
    {
    	try(PrintWriter out = new PrintWriter("tic-tac-toe-4.csv"))
    	{
    		Iterator<String> it = myBoards.iterator();
    		
    		while(it.hasNext())
    		{
    			out.println(it.next());
    		}
    		
    	}catch (FileNotFoundException e) {
			
			e.printStackTrace();
    	}
    }
    
    static int win[][] = {{0, 1, 2, 3},   
    	    {4, 5, 6, 7},   
    	    {8, 9, 10, 11},   
    	    {12, 13, 14, 15},
    	    {0, 4, 8, 12},
    	    {1, 5, 9, 13},  
    	    {2, 6, 10, 14}, 
    	    {3, 7, 11, 15}, 
    	    {0, 5, 10, 15}, 
    	    {3, 6, 9, 12}}; 
    	  
   
    	    static boolean isCWin(char[] board, char c) { 
    	          
    	        for (int i = 0; i < 10; i++) { 
    	            if (board[win[i][0]] == c 
    	                    && board[win[i][1]] == c 
    	                    && board[win[i][2]] == c
    	                    && board[win[i][3]] == c) { 
    	                return true; 
    	            } 
    	        } 
    	        return false; 
    	    } 
    
    static boolean isValid(char board[]) { 
         
        int xCount = 0, oCount = 0, plusCount = 0; 
        for (int i = 0; i < 16; i++) { 
            if (board[i] == 'X') { 
                xCount++; 
            } 
            if (board[i] == 'O') { 
                oCount++; 
            }
            
            if (board[i] == '+') { 
            	plusCount++; 
            } 
        } 
  
  
        if (xCount == oCount || xCount == plusCount || xCount == oCount + 1 || xCount == plusCount + 1 || oCount == plusCount + 1) 
        { 
             
            if (isCWin(board, 'O')) { 
                 
                if (isCWin(board, 'X')) { 
                    return false; 
                }
                
                if (isCWin(board, '+')) { 
                    return false; 
                }
  
                 
                return (xCount == oCount && oCount == plusCount + 1); 
            }
            
           
            if (isCWin(board, '+')) { 
               
                if (isCWin(board, 'X')) { 
                    return false; 
                }
                                   
                if (isCWin(board, 'O')) { 
                    return false; 
                }
  
                  
                return (xCount == plusCount && oCount == plusCount);
            } 
              
            if (isCWin(board, 'X') && (xCount != oCount + 1 || xCount != plusCount + 1)) { 
                return false; 
            }
  
              
            return true; 
        } 
        return false; 
    } 
    
    public static void main(String[] args) {
    	TicTacToeValidCombinations tt = new TicTacToeValidCombinations();
    	tt.addCombinations();
    	tt.outputToFile();
    }
}
