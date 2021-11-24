using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Leopotam.Ecs;

public class EcsStartup : MonoBehaviour
{
    private EcsWorld ecsWorld;
    private EcsSystems systems;

    private void Start()
    {
        ecsWorld = new EcsWorld(); // ������� ����� EcsWorld
        systems = new EcsSystems(ecsWorld); // � ������ ������ � ���� ����

        systems.Init();
        //systems
        //    .Add(new PlayerInitSystem()) // ��������� ������ �������
        //    .Init(); // ����������� �������������� ������ ������
    }

    private void Update()
    {
        systems?.Run(); // ��������� ������� ������ ����
    }

    private void OnDestroy()
    {
        systems?.Destroy(); // ���������� ������ ������ ��� ����������� ��������
        systems = null;
        ecsWorld?.Destroy(); // � ���
        ecsWorld = null;
    }
}