package com.dash.dashboard.scraper.java;

import com.dash.dashboard.scraper.java.ToolsTables;
import com.dash.dashboard.views.dashboard.Announcement;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class AnnouncementsTable extends ToolsTables {
    private Connection connection;

    public AnnouncementsTable(){
        connection = super.connect();
    }
    
    public List<Announcement> announcementsList(){
        List<Announcement> announcements = new ArrayList<>(0);
        try {
            ResultSet rs = this.selectAll();
            // loop through the result set
            if (rs != null){
                while (rs.next()) {
                    String preview = rs.getString("Preview");
                    preview = preview.substring(preview.indexOf("t")+2);
                    announcements.add(new Announcement(preview,
                            rs.getString("Author"),
                            rs.getString("Date"),
                            rs.getString("Link")));
                }
            }
        }catch (SQLException e){
        }
        return announcements;
    }


    @Override
    public ResultSet selectAll() {
        String sql = "SELECT Preview, Author, Date, link  FROM Announcements";
        ResultSet rs;
        try{
            Statement stmt  = this.connection.createStatement();
            rs    = stmt.executeQuery(sql);
            return rs;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return null;
    }

    @Override
    public void printAll() {
        ResultSet rs = this.selectAll();
        // loop through the result set
        try {
            while (rs.next()) {
                System.out.println(rs.getString("Preview") + "\t" +
                        rs.getString("Author") + "\t" +
                        rs.getString("Date") + "\t" +
                        rs.getString("link"));
            }
        }catch (SQLException e){
            System.out.println(e.getMessage());
        }
    }

}
