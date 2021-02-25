package com.dash.dashboard.views.dashboard;

import com.dash.dashboard.scraper.java.GradebookTable;

import java.util.concurrent.ThreadPoolExecutor;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class Gradebook {
    private String Course, Title, Mark, Total;

    public Gradebook(String Course, String Title, String Mark,String Total){
        this.Course = Course;
        this.Title = Title;
        this.Mark = Mark;
        this.Total = Total;
    }

    public String getTitle(){return Title;}

    public String getCourse(){return Course;}

    public String getMark(){return Mark;}

    public String getTotal(){
        return Total;
    }
}
