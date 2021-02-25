package com.dash.dashboard.views.dashboard;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class Test {
    private String title, time_limit, due_date;

    public Test(String Title,String TimeLimit,String DueDate){
        title = Title;
        time_limit = TimeLimit;
        due_date = DueDate;
    }

    public String getTitle(){
        return title;
    }

    public String getTimeLimit(){
        return time_limit;
    }

    public String getDueDate(){
        return due_date;
    }


}
