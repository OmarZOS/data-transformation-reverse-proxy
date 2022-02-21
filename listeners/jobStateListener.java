package listeners;


import java.util.Iterator;



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.spark.scheduler.*;
import org.apache.http.*;



public class jobStateListener extends SparkListener {
    
    String STATE_LISTENER_HOST = System.getenv("SPARK_JOB_LISTENER_HOST");
    String STATE_LISTENER_PORT = System.getenv("SPARK_JOB_LISTENER_PORT");
   
   
    @Override
    public void onJobEnd(SparkListenerJobEnd stageCompleted) {
    try {
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost("http://www.a-domain.com/foo/");

        // Request parameters and other properties.
        List<NameValuePair> params = new ArrayList<NameValuePair>(2);
        params.add(new BasicNameValuePair("param-1", "12345"));
        params.add(new BasicNameValuePair("param-2", "Hello!"));
        httppost.setEntity(new UrlEncodedFormEntity(params, "UTF-8"));

        //Execute and get the response.
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                // do something useful
            }
        }
    }
    catch(Exception e) {

    }
   }
}