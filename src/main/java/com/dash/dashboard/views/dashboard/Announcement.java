package com.dash.dashboard.views.dashboard;

import com.vaadin.server.ExternalResource;
import com.vaadin.ui.Link;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class Announcement {
    private String Preview;
    private String Author;
    private String Date;
    private String link;

    public Announcement(String Preview, String Author, String Date,String link){
        this.Preview = Preview;
        this.Author = Author;
        this.Date = Date;
        this.link = link;
    }

    public String getPreview(){
        return Preview;
    }

    public String getAuthor(){
        return Author;
    }

    public String getDate(){
        return Date;
    }


//    public Link getClickMe(){
//        Link link = new Link("Click Me!",
//                new ExternalResource("http://vaadin.com/"));
//        link.isConnectorEnabled();
//        return link;
//    }

}
