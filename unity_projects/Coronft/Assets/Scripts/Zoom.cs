using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zoom : MonoBehaviour
{
    Camera _cam;

    int _current = 0;
    public int Current
    {
        get { return _current; }
        set
        {
            if (value < min)
                _current = min;
            else if (value > max)
                _current = max;
            else
                _current = value;
            ChangeCameraZoom();
        }
    }


    [SerializeField] int min;
    [SerializeField] int max;
    const int real_max = 40;

    

    private void ChangeCameraZoom()
    {
        _cam.orthographicSize = 2602 - Mathf.Lerp(0, 2595, (float)Current/real_max);
    }

    public void PlusZoom()
    {
        Current++;
        ChangeCameraZoom();
    }

    public void MinusZoom()
    {
        Current--;
        ChangeCameraZoom();
    }


    // Start is called before the first frame update
    void Start()
    {
        _cam = GetComponent<Camera>();
        Current = min;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
