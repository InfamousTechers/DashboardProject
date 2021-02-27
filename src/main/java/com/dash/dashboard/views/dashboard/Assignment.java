package com.dash.dashboard.views.dashboard;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class Assignment{
    private String Site;
    private String Title;
    private String DueDate;

    public Assignment(String Site, String Title, String DueDate){
        this.Site = Site;
        this.Title  = Title;
        this.DueDate = DueDate;
    }

    public String getSite(){
        return Site;
    }

    public String getTitle(){
        return Title;
    }

    public String getDueDate(){
        return DueDate;
    }
}

