package com.dash.dashboard.scraper.java;

import java.sql.Connection;
import java.sql.ResultSet;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public interface Tables {

    String url = "jdbc:sqlite:src/main/java/com/dash/dashboard/scraper/python/VulaTools.db";

    Connection connect();

    ResultSet selectAll();

}
