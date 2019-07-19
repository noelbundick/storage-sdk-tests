// 196390

package com.example;

import java.io.IOException;

import org.junit.Test;
import static org.junit.Assert.*;

import com.azure.storage.blob.BlockBlobClient;

public class BlobTest 
{
    @Test
    public void shouldUploadWithFolderNameWithLeadingSlash() throws IOException
    {
        String connString = System.getProperty("connString");
        BlockBlobClient client = BlockBlobClient.blockBlobClientBuilder()
            .connectionString(connString)
            .containerName("testcontainer")
            .blobName("/folder1/nestedfolder2/nestedfolder3/helloworld.txt")
            .buildClient();
        client.uploadFromFile("/mnt/c/code/noelbundick/storage-sdk-tests/data/loremipsum.txt");

        String blobUrl = client.getBlobUrl().toString();
        int index = blobUrl.indexOf("//folder1");
        assertTrue(blobUrl, index == -1);
    }

    @Test
    public void shouldUploadWithFolderNameWithoutLeadingSlash() throws IOException
    {
        String connString = System.getProperty("connString");
        BlockBlobClient client = BlockBlobClient.blockBlobClientBuilder()
            .connectionString(connString)
            .containerName("testcontainer")
            .blobName("folder1/nestedfolder2/nestedfolder3/helloworld.txt")
            .buildClient();
        client.uploadFromFile("/mnt/c/code/noelbundick/storage-sdk-tests/data/loremipsum.txt");

        String blobUrl = client.getBlobUrl().toString();
        int index = blobUrl.indexOf("//folder1");
        assertTrue(blobUrl, index == -1);
    }
}
