using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using UnityEngine;


public struct Point
{
    public float x;
    public float y;

    public Point(float _x, float _y)
    {
        x = _x;
        y = _y;
    }
};

[System.Serializable]
public class Letter
{
    public Sprite sprite;
    public int num;
};

public class PointGenerator : MonoBehaviour
{
    [SerializeField] private GameObject _prebaf_point;
    [SerializeField] private Transform _parent;

    [SerializeField] private List<Letter> letters;

    // Start is called before the first frame update
    List<Point> points = new List<Point>();
    void Start()
    {
        TextAsset txt = Resources.Load<TextAsset>("letter_coords");
        List<string> lines = new List<string>(txt.text.Split('\n'));
        foreach (var line in lines)
        {
            List<string> nums = new List<string>(line.Split(' '));
            float x = float.Parse(nums[0], CultureInfo.InvariantCulture.NumberFormat), y = float.Parse(nums[1], CultureInfo.InvariantCulture.NumberFormat);
            //points.Add(new Point(x*10, y*10));
            points.Add(new Point(x * 12, y * 12));
        }
        Debug.Log(points.Count);

        //var _points = new List<Point>(points.ToArray());
        
        foreach (var letter in letters)
        {
            for (int i = 0; i < letter.num; i++)
            {
                int pos = Random.Range(0, points.Count);
                Point point = points[pos];
                points.RemoveAt(pos);
                SpriteRenderer obj = Instantiate(_prebaf_point, new Vector3(point.x, point.y, 0), _parent.rotation, _parent).GetComponent<SpriteRenderer>();
                obj.sprite = letter.sprite;
            }
        }
        
        //foreach (var coord in points)
        //{
        //    Instantiate(_prebaf_point, new Vector3(coord.x, coord.y, 0), _parent.rotation, _parent);
        //}



    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
